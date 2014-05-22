-- Send email alerts to watchlists
-- ONE email per address
begin
    set nocount on
    
    begin try
                
        declare @depot char(2)
        declare @stockid bigint
        declare @address varchar(512)
        declare @message varchar(max)

        declare @alerts table (stock int, depot char(2), product varchar(32), source char(2), [description] varchar(255), email varchar(512), sent bit, low decimal(10,4), total decimal(10,4))
        declare @action table (email varchar(255), [message] varchar(max))

        begin tran

        insert into @alerts(stock, depot, product, source, [description], email, sent, low, total) 
        select id, depot, product_code, source, [description], email, sent, low, total 
          from stock_report where email is not null and isnull(sent, 0) = 0 and total < low

        while exists (select 1 from @alerts)
        begin

            select top 1
                   @stockid = stock
                 , @depot = depot
                 , @address = email
                 , @message = convert(varchar, total) + ' @ ' + @depot + ' ' + product + ' - ' + [description]
              from @alerts
             order by email
            
            insert into @action (email, [message]) select item, @message from dbo.List(@address)

            delete from @alerts where stock = @stockid

            update stock set sent = 1 where id = @stockid
        end

        while exists (select 1 from @action)
        begin

            select top 1
                   @address = email
                 , @message = 'Please note the following alerts:'+char(10)+char(10)+'http://gbrsdheid0002/REPORTS/Pages/ReportViewer.aspx?%2fCOPS%2fStock&rs:Command=Render'+char(10)+char(10)
              from @action
             order by email

            select @message = coalesce(@message, '') + [message] + char(10) 
              from @action
             where email = @address
             order by email

            delete from @action where email = @address

            exec msdb.dbo.sp_send_dbmail @profile_name = 'SQL Admin', @recipients = @address, @subject = 'Stock Alert Report', @body = @message

        end

        commit tran 
    end try 
    begin catch

        select @message = 'error: ' + convert(varchar(32), @@ERROR) + ' - ' + error_message() + '-- ' + @message
        print @message  

        rollback    
        exec xp_logevent 60000, @message, error

    end catch
    
end
