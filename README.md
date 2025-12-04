# Theoria

[![tests](https://github.com/KYLChiu/theoria/actions/workflows/tests.yml/badge.svg)](https://github.com/KYLChiu/theoria/actions/workflows/tests.yml)
[![commit](https://github.com/KYLChiu/theoria/actions/workflows/commit.yml/badge.svg)](https://github.com/KYLChiu/theoria/actions/workflows/commit.yml)

## Goal

```cpp
                                                                                                    
                                          .--=:::::==+===:.      .:==-=:                            
                                       .:::.-:.:--       :=---:  ..::::-..                          
                                     .........-   - ..--:......  .:::.                              
                                   .:: :.::.   .: :. :::--:::::-.                                   
                                  ..=:..::.:..:::-..::    .-=.                                      
                                  :-:.. :::- :.-..      --:                                         
                                 .:..:.-:.            :-.                                           
                                 :::::::          . .--.                                            
                                 :::::-:         ::.::                                              
                                 .. :.....:::-:-::--:                                               
                                 ..              .:--                                               
                                 :.              ::--=-                                             
                                 :.         .--::-:.:-::-.                                          
                                 ..:::.  .--------:.:--===-                                         
                                :::    .::::::.::::.:..::--=:                                       
                               .....  ..::::.:.:.:::::..:.:-=:                                      
                              .:...   .--:.::::-:-:::::.:..:=-.                                     
                             .-::.. .-- . ::=-.-.. ..:::- .:-=.                                     
                             :.:::.  ::.::.::::::....::::. ..::                                     
                           .-::--:.:::::-.:::..:. ... ..::...:-.                                    
                           :::::.  :.:-..:::.::......::.::....--                                    
                         .-:::..-   ..:::..:::...:...:..:: ...:=-                                   
                         :.-:: .: :-:::-:::-:--:.:.:.--.. ::.::=:::                                 
                        --::::.:: :-: .::.-:::::..::.--:--::..:-::-+.                               
                       .=:...:::: ....:.::::.......:.:... . ...-::::-.                              
                       :: :::: .. :-:.::-:::::::-: ::-::-:.: .:=-::.:=.                             
                      .::::.::... :.::..:::-::--:::-:::.:.....---.::::-:                            
                      ::::.::::::  .::-:-::--:.-:.-:::-:::.....-:.::.::+:.                          
                      ::......:::  ...:::::::.::..:.......:::.:=- :-:..+-.                          
                     .... .:::::. :-  .:.....::::.....:. .:-::-=-  =-..-+:                          
                     .-:::..:::-  :-:.::--=-:---=.:::..::- ...:-:   =::.=-                          
                     ::....:-:::  : .::--::-:=----:..::.: ...:-:    .:::==.                         
                     :-:::.::.:   ::.  ::..::...::::.::.. :.::-.     -:.:-                          
                     -:::..:-::   . ...::...:..: ......-=::::-:      .-:-=.                         
                     .-:::.::. .....-::.::..-::-:::::::.::::=:       .-:.-                          
                      :-.--..:-::.:-...-:-.::.::--:-.:..:..=-.        --:                           
                       ::.::....:. .:::::::.::::---::..:::--:                                       
                       .=-:..-::-:----=.:-:..:----...::::=:                                         
                        -+-:::..:::...:::...::..::-::..:=:                                          
                       .:==:.:::-.:- .--::-.::.--::.:::--                                           
                       :..=---:::...::..........:. :-.-=.                                           
                     ::. :-==++++=- ::.::::.:: .:-::-++==--:::.                                     
                         =-#+-+*:==:=*#:-.      .==----=*=-=##*+=-=***=                             
                           -=  .*-      --                    -= ...   .                            
```

We provide jupyter notebooks to learn:

- **Computer Science**
- **Software Development**
- **Statistics**
- **Mathematics**
- **Quantitative Finance**

Notebooks are labeled as follows:

- **Basic**: For beginners, covering the essentials.
- **Intermediate**: For those with some experience, ready to explore more.
- **Proficient**: For practitioners or those with a deeper interest in the subject.

## Setup 

1. Follow the installation guide of the [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

2. Once `uv` is installed, run
```bash
uv sync --all-extras
```

## Run

### Jupyter Lab

Simply run the notebooks via:
```bash
uv run jupyter lab
```

### VSCode

Upon completing the setup, the python executable is located at:
```bash
.venv/bin/python
```
which can be used as the jupyter kernel.

Happy learning!