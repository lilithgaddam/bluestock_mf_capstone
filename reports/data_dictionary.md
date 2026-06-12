# Data Dictionary

## fund_master.csv

| Column       | Type    | Description              |
| ------------ | ------- | ------------------------ |
| amfi_code    | Integer | Unique AMFI scheme code  |
| scheme_name  | Text    | Mutual fund scheme name  |
| fund_house   | Text    | Asset management company |
| category     | Text    | Fund category            |
| sub_category | Text    | Fund sub category        |

## nav_history.csv

| Column    | Type    | Description       |
| --------- | ------- | ----------------- |
| amfi_code | Integer | Scheme identifier |
| date      | Date    | NAV date          |
| nav       | Decimal | Net Asset Value   |

## investor_transactions.csv

| Column           | Type    | Description              |
| ---------------- | ------- | ------------------------ |
| investor_id      | Integer | Investor identifier      |
| amfi_code        | Integer | Scheme identifier        |
| amount           | Decimal | Transaction amount       |
| transaction_type | Text    | SIP, Lumpsum, Redemption |

## scheme_performance.csv

| Column       | Type    | Description                 |
| ------------ | ------- | --------------------------- |
| return_1yr   | Decimal | One year return             |
| return_3yr   | Decimal | Three year return           |
| return_5yr   | Decimal | Five year return            |
| sharpe_ratio | Decimal | Risk adjusted return metric |
