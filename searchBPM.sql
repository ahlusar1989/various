-- ngf 2014 find bad codez
-- exec lombardi.searchBPM 'bad codez'
create procedure searchBPM (@text varchar(max)) as 
select p.name [process]
     , i.name [step]
     , s.last_modified as [date modified]
     , full_name as author
     , comments
     , code
from 
     (select distinct twcomponent_id, name, process_id from lombardi.lsw_process_item) i
join (select distinct process_id, name from lombardi.lsw_process) p on i.process_id = p.process_id
join (select script_id
           , s.version_id
           , s.last_modified
           , full_name
           , convert(varchar(max), convert(varbinary(max), script, 2)) as code -- eg 0x764B1A4...
        from lombardi.lsw_script s
        join lombardi.lsw_usr_xref u on s.last_modified_by_user_id = u.user_id
       where s.version_id in (
        select distinct version_id
        from lombardi.lsw_script s
        join (select script_id
                   , max(last_modified) as latest
                from lombardi.lsw_script s 
               group by script_id) f on f.script_id = s.script_id and f.latest = s.last_modified)
     ) s on i.twcomponent_id = s.script_id 
cross apply (select top 1 description comments from lombardi.lsw_process where process_id = p.process_id) l
where (@text is null or code like '%'+@text+'%') 
order by last_modified desc

