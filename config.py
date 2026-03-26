"""
docstring for config
"""

print("""

\033[1;37m
___                              ___                                                                                     
`MM                 68b          `MM                                                                                     
 MM                 Y89           MM         /                /                                                          
 MM   __  ___  __   ___   __      MM  __    /M       ____    /M       _____   ___   ___ ___  __     __ ____   ____    ___
 MM   d'  `MM 6MMb  `MM  6MMbMMM  MM 6MMb  /MMMMM   6MMMMb\ /MMMMM   6MMMMMb  `MM    MM `MM 6MM     `M6MMMMb  `MM(    )M'
 MM  d'    MMM9 `Mb  MM 6M'`Mb    MMM9 `Mb  MM     MM'    `  MM     6M'   `Mb  MM    MM  MM69 "      MM'  `Mb  `Mb    d' 
 MM d'     MM'   MM  MM MM  MM    MM'   MM  MM     YM.       MM     MM     MM  MM    MM  MM'         MM    MM   YM.  ,P  
 MMdM.     MM    MM  MM YM.,M9    MM    MM  MM      YMMMMb   MM     MM     MM  MM    MM  MM          MM    MM    MM  M   
 MMPYM.    MM    MM  MM  YMM9     MM    MM  MM          `Mb  MM     MM     MM  MM    MM  MM          MM    MM    `Mbd'   
 MM  YM.   MM    MM  MM (M        MM    MM  YM.  , L    ,MM  YM.  , YM.   ,M9  YM.   MM  MM     68b  MM.  ,M9     YMP    
_MM_  YM.__MM_  _MM__MM_ YMMMMb. _MM_  _MM_  YMMM9 MYMMMM9    YMMM9  YMMMMM9    YMMM9MM__MM_    Y89  MMYMMM9       M     
                        6M    Yb                                                                     MM           d'     
                        YM.   d9                                                                     MM       (8),P      
                         YMMMM9                                                                     _MM_       YMM   

""")



headless_option = input("Please input 1 for headless mode, or 0 for visual mode: \n")
size = int(input("provide grid size: "))

if headless_option == "0":
    import pygame
    pygame.init
    sample_surface = pygame.display.set_mode((800,800))
    f = 0
else:
    f = 1