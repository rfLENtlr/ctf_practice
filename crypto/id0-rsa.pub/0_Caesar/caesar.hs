import Data.Char as C

caesars :: String -> IO ()
caesars s = mapM_ putStrLn [ caesar n (s ++ "\n") | n <- [1..26]]

caesar k = map (rot k) 

rot k c | isLower c = chr $ (ord c - ord 'a' + k) `mod` 26 + ord 'a'
        | isUpper c = chr $ (ord c - ord 'A' + k) `mod` 26 + ord 'A'
        | otherwise = c
