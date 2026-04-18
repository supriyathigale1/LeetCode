# LeetCode
Practice Leetcode Python Solutions

## Solutions Included

### 1. Rearrange Spaces Between Words
- **File:** `Strings/rearrange_spaces.py`
- **Alternate Implementation:** `Strings/my_reorderspaces.py`
- **Tests:** `tests/test_rearrange_spaces.py`
- **Description:** Rearranges spaces between words evenly, with extra spaces placed at the end.

### 2. Convert a Number to Hexadecimal
- **File:** `Strings/to_hex.py`
- **Description:** Converts a 32-bit signed integer to its hexadecimal representation.

### 3. Add Binary
- **File:** `Strings/add_binary.py`
- **Description:** Adds two binary strings and returns their sum as a binary string.

### 4. Add Strings
- **File:** `Strings/add_strings.py`
- **Description:** Adds two non-negative integers represented as strings and returns their sum as a string.

### 5. Convert to Excel Column Title
- **File:** `Strings/convert_to_title.py`
- **Description:** Converts a column number to its corresponding Excel column title.

### 6. Title to Number
- **File:** `Strings/title_to_number.py`
- **Description:** Converts an Excel column title to its corresponding column number.

### 8. Find Words Containing Character
- **File:** `Strings/find_words.py`
- **Description:** Finds words in a list that contain a given character.

### 9. Fizz Buzz
- **File:** `Strings/fizz_buzz.py`
- **Description:** Returns a list of strings representing numbers from 1 to n, with multiples of 3 and 5 replaced by "Fizz" and "Buzz".

### 10. Repeated Substring Pattern
- **File:** `Strings/repeated_substring.py`
- **Description:** Checks if a string can be constructed by repeating a substring.

### 11. Pascal's Triangle
- **File:** `Arrays/pascals_triangle.py`
- **Description:** Generates Pascal's triangle up to a given number of rows.

### 12. Range Sum Query
- **File:** `Arrays/sum_range.py`
- **Description:** Implements range sum query operations.

### 13. Find First and Last Position of Element in Sorted Array
- **File:** `Arrays/search_range.py`
- **Description:** Finds the first and last position of a target element in a sorted array.

### 14. Third Maximum Number
- **File:** `Arrays/third_max.py`
- **Description:** Finds the third maximum unique number in an array.

### 15. Find All Numbers Disappeared in an Array
- **File:** `Arrays/find_disappeared_numbers.py`
- **Description:** Finds all numbers in range [1, n] that are missing from the array.

### 16. Intersection of Two Arrays II
- **File:** `Arrays/intersect_arrays.py`
- **Description:** Finds the intersection of two arrays with duplicate handling.

### 17. Deduplication of Events
- **File:** `Arrays/deduplication_array.py`
- **Description:** Deduplicates events based on user_id and event type, keeping the latest timestamp.

### 18. Event Sessionization
- **File:** `Arrays/sessionization.py`
- **Description:** Groups events into sessions based on a 30-minute time gap threshold.

### 19. Moving Average from Data Stream
- **File:** `Arrays/moving_avg`
- **Description:** Calculates the moving average of a stream of numbers.

### 20. Flatten Nested JSON
- **File:** `Dictionary/flatten_nested_json.py`
- **Description:** Flattens nested dictionary structures into a single-level dictionary with concatenated keys.

### 21. Top K Frequent Elements
- **File:** `Dictionary/top_k_frequent_elements.py`
- **Description:** Returns the k most frequent elements from a list using Counter.

### 22. Error Log Filtering
- **File:** `Files/logging.py`
- **Description:** Filters and extracts error logs from a list of log entries.

### 23. Partition File into Chunks
- **File:** `Files/partition_file.py`
- **Description:** Chunks data into fixed-size partitions using a generator.

### 24. Transform CSV Data
- **File:** `Files/transform_csv.py`
- **Description:** Reads CSV file, transforms data (uppercase names, convert age to int), and writes to new CSV.

### 25. Idempotent Payment Processing
- **File:** `Set/idempotency_payment.py`
- **Description:** Implements idempotent payment processing using a set to track processed payment IDs.

### 26. Retry Logic with Exponential Backoff
- **File:** `Opex/retry_logic.py`
- **Description:** Implements retry logic with configurable retries and delay between attempts.

### 27. Bronze Layer (Medallion Architecture)
- **File:** `Medallion/bronze_layer.py`
- **Description:** Code for the bronze layer in medallion architecture.

### 28. Silver Layer (Medallion Architecture)
- **File:** `Medallion/silver_layer.py`
- **Description:** Code for the silver layer in medallion architecture.

## Usage

Run tests for Rearrange Spaces:

```bash
python3 -m unittest discover -s tests
```

Run any solution:

```bash
python3 <solution_file.py>
```
