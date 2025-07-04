SELECT 
    c."Location",
    c."Country",
    COUNT(r."RaceId") AS "Number of Races"
FROM test.races r
JOIN test.circuits c 
    ON r."CircuitId" = c."CircuitId"
WHERE c."Location" ~ '^[A-Za-z\s]+$'  -- Only alphabetic and space characters
GROUP BY c."Location", c."Country"
HAVING COUNT(r."RaceId") > 0
ORDER BY "Number of Races" DESC
LIMIT 5;
