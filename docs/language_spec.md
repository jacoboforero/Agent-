### **Commands:**

### **1. Workflow Management**

These commands are fundamental for defining and orchestrating multi-step tasks:

- `task <name>`: Define a reusable task.
- `execute <task>`: Run a defined task or system command.
- `parallel`: Execute multiple tasks concurrently.
- `wait <task>`: Wait for a task to complete.
- `schedule <task> at <time>`: Schedule tasks for future execution.

---

### **2. File and Data Operations**

For managing files, directories, and data:

- `read <file>`: Read the contents of a file.
- `write <data> to <file>`: Write data to a file.
- `delete <file>`: Remove a file or directory.
- `move <file> to <destination>`: Move files or directories.
- `compress <files> > <archive>`: Create compressed archives.
- `extract <archive>`: Extract compressed files.
- `list <directory>`: List files in a directory.

---

### **3. Network and API Interactions**

To enable integration with external systems:

- `fetch <url>`: Retrieve data from a URL.
- `send <data> to <url>`: Post data to a URL or API.
- `query_api <url>`: Query an API endpoint and return structured results.
- `upload <file> to <destination>`: Upload files to cloud services or servers.
- `download <file> from <url>`: Download files from URLs.

---

### **4. System Operations**

For interacting with the operating system safely:

- `shell <command>`: Execute shell commands in a sandboxed environment.
- `log <message>`: Log events or messages.
- `alert <message>`: Send an alert to the user.
- `current_time`: Retrieve the current system time.

---

### **5. Data Manipulation**

Built-in commands for common data-processing tasks:

- `filter < (Work in Progress, not implemented)`data> where <condition>`: Extract elements matching a condition.
- `transform < (Work in Progress, not implemented)`data> with <function>`: Apply transformations to data.
- `sort <data> by <key>`: Sort data by specified criteria.
- `aggregate < (Work in Progress, not implemented)`data> using <function>`: Aggregate data (e.g., sum, average).

---

### **6. Decision-Making and Control Flow**

For enabling agentic behavior and decision-making:

- `if <condition>:`: Conditional execution.
- `else:`: Alternate execution path.
- `loop <task> until <condition>`: Repeat tasks until a condition is met.
- `on_error <task>`: Specify actions to perform if a task fails.

---

### **8. Interaction with LLMs**

For AI-driven automation tasks:

- `analyze < (Work in Progress, not implemented)`data> with <model>`: Run AI analysis on data.
- `summarize < (Work in Progress, not implemented)`data>`: Generate a summary from text or structured data.
- `predict < (Work in Progress, not implemented)`input> using <model>`: Perform predictions with an AI model.
- `train < (Work in Progress, not implemented)`model> with <data>`: Train an AI model (sandboxed to prevent unintended resource use).

---

### **9. Communication and Notifications**

For sending messages or notifications:

- `notify <recipient>`: Send a notification to a user or system.
- `email <sender><recipient>`: Send an email with specified content.
- `log_message <message>`: Log detailed information for debugging.

---

### **Examples:**

#### 1. Hello World

```plaintext
task hello_world:
    print "Hello, Agent++!"
    execute "echo 'System ready'"
```

#### 2. Backup Task

```plaintext
task backup:
    compress /home/user/documents > backup.zip
    upload backup.zip to cloud_storage
    log "Backup completed at $(current_time)"
```

#### 3. Automated Data Fetching

```plaintext
task fetch_and_store:
    data = fetch "https://api.example.com/data"
    write data to latest_data.json
    log "Data fetched and stored."
```

#### 4. Multi-Step Data Processing

```plaintext
task process_logs:
    logs = read /var/logs/*.log
    errors = filter logs where line.contains("ERROR")
    write errors to error_summary.txt
    log "Processed logs and saved error summary."
```

#### 5. Multi-Task Workflow

```plaintext
task daily_report:
    execute fetch_and_store
    execute process_logs
    log "Daily report tasks completed."
```

#### 6. Simple Decision-Making

```plaintext
task analyze_data:
    data = fetch "https://api.example.com/data"
    if data.size > 100MB:
        log "Large dataset detected, preparing resources."
    else:
        log "Dataset size is manageable."
    write data to processed_data.json
```

#### 7. File Organization

```plaintext
task organize_files:
    move *.jpg to /photos/
    move *.mp4 to /videos/
    delete /temp/*.tmp
    log "File organization complete."
```

#### 8. Basic LLM Integration

```plaintext
task summarize_data:
    data = read /home/user/data.txt
    summary = summarize data
    write summary to summary.txt
    log "Data summarized and saved."
```

#### 9. Data Transformation Pipeline

```plaintext
task clean_and_transform:
    raw_data = read raw_data.csv
    clean_data = transform raw_data with remove_nulls()
    save clean_data to clean_data.csv
    log "Data cleaned and saved."
```

#### 10. API Query and Conditional Processing

```plaintext
task fetch_weather:
    response = query_api "https://api.weather.com/current"
    if response.status == "success":
        log "Weather data fetched successfully."
        write response.payload to weather_data.json
    else:
        log "Failed to fetch weather data."
```

#### 11. Concurrent Execution

```plaintext
task handle_multiple_tasks:
    parallel:
        execute backup
        execute fetch_and_store
    log "All tasks completed in parallel."
```

---

### **Formal Syntax Rules**

```ebnf
<program>       ::= { <task-definition> } .

<task-definition> ::= "task" <identifier> ":" <block> .

<block>         ::= { <statement> } .

<statement>     ::= <command> | <conditional> | <loop> | <assignment> | <execution> | <log> .

<command>       ::= "read" <filepath>
                  | "write" <expression> "to" <filepath>
                  | "delete" <filepath>
                  | "move" <filepath> "to" <destination>
                  | "compress" <files> ">" <archive>
                  | "extract" <archive>
                  | "fetch" <url>
                  | "upload" <filepath> "to" <destination>
                  | "download" <filepath> "from" <url> .

<conditional>   ::= "if" <condition> ":" <block> [ "else:" <block> ] .

<loop>          ::= "loop" <block> "until" <condition> .

<assignment>    ::= <identifier> "=" <expression> .

<execution>     ::= "execute" <task-call>
                  | "parallel:" <block>
                  | "wait" <task-call>
                  | "schedule" <task-call> "at" <time> .

<task-call>     ::= <identifier> [ "(" <arguments> ")" ] .

<log>           ::= "log" <string> .

<expression>    ::= <literal>
                  | <identifier>
                  | <function-call>
                  | <arithmetic-expression> .

<function-call> ::= <identifier> "(" <arguments> ")" .

<condition>     ::= <expression> <comparison-operator> <expression> .

<comparison-operator> ::= "==" | "!=" | ">" | ">=" | "<" | "<=" .

<arithmetic-expression> ::= <expression> <arithmetic-operator> <expression> .

<arithmetic-operator> ::= "+" | "-" | "*" | "/" .

<arguments>     ::= <expression> { "," <expression> } .

<literal>       ::= <string> | <number> | <boolean> .

<identifier>    ::= <letter> { <letter> | <digit> | "_" } .

<filepath>      ::= <string> .

<files>         ::= <string> { "," <string> } .

<archive>       ::= <string> .

<url>           ::= <string> .

<string>        ::= "\"" { <character> } "\"" .

<number>        ::= [ "-" ] <digit> { <digit> } .

<boolean>       ::= "true" | "false" .

<time>          ::= "\"" <ISO-8601 timestamp> "\"" .
```
