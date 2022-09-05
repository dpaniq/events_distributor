# Events Randomizer

## How the config looks like

The config available format is `json/yaml` file

### Example

 > **filename_path_of_events**
 Absolute path to event file from this directory
 Example: 

 > **experts**: 
 Columns number
 Example: *30*

 > **experts**: 
 Rows number
 Example: *10*

 > **segment_name**
 Bad symbols in name \` - ' - "

#### Config interface
```
    interface Config {
        events: [
            {
                name: string
                segments: [
                    {
                        name: string
                        columns: number
                        rows: number
                    },
                    {
                        name: string
                        columns: number
                        rows: number
                    },
                ]
            }
        ]
    }
```

#### Yaml `config.yaml`

```

    segment_path: <filename_path_of_events>
    experts: 
    time

  ```

#### JSON `config.json`



### The original files safe
The script does not change the source files

```
    - Don't worry. Be happy" - Bob Marley
```