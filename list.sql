ALTER FUNCTION [dbo].[List]
(
	@List varchar(max)
)
RETURNS 
@ParsedList table
(
	Item varchar(32)
)
AS
BEGIN
	DECLARE @Item varchar(32), @Pos int

	SET @List = LTRIM(RTRIM(@List))+ ','
	SET @Pos = CHARINDEX(',', @List, 1)

	IF REPLACE(@List, ',', '') <> ''
	BEGIN
		WHILE @Pos > 0
		BEGIN
			SET @Item = LTRIM(RTRIM(LEFT(@List, @Pos - 1)))
			IF @Item <> ''
			BEGIN
				INSERT INTO @ParsedList (Item) 
				VALUES (CAST(@Item AS varchar)) --Use Appropriate conversion
			END
			SET @List = RIGHT(@List, LEN(@List) - @Pos)
			SET @Pos = CHARINDEX(',', @List, 1)

		END
	END	
	RETURN
END

