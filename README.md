# FoxyProxy Config Rollback

The project can modify the config file of FoxyProxy with 8.1-8.2 back to 7.5 friendly version.

## Usage

First, clone the project:

`git clone https://github.com/ohitworks/FoxyProxy-Config-Rollback.git --depth=1`

Then `cd FoxyProxy-Config-Rollback` and run `python3 main.py`.

You can input the new-type config path and old-type config path in the terminal. Or run the file with `python3 ./main.py <old path> <save path>`.

## Note

You maybe find your pattern config of `https` and `http` changed to `both http and https`. I'm sorry for that because all my config is `both ...` so all config will be write as that. You can update the python function `pattern_modify` by your self. Hope your PR. :hand:
