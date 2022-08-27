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

#### Interface
```

    interface Config {
        config_name: event_path
        event_path: event_path 
        segments: [
            {
                event_path: string
                columns: number
                rows: number
            },
            {
                columns: number
                rows: number
            },
            ...
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