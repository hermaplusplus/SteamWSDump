# SteamWSDump

Simple modifiable script for dumping Steam Workshop file/object/mod names from a list of IDs in the repeating form `@FILEID0001;`.

Compatible with ARMA 3 mod load order strings.

## Usage

In this first iteration of the script, arguments cannot be passed. To configure it, replace `API_KEY_HERE` with your Steam API key (register or view yours [here](https://steamcommunity.com/dev/apikey)) and the contents of `_MLO` with the series of IDs in the repeating form `@FILEID0001;`.

Run the file and a CSV output (`ID,name`) will be printed to the terminal. Uncomment line 16 to see all data returned from the first ID in `_MLO` for debugging/development purposes.

Some official documentation can be found [here](https://steamcommunity.com/dev).
