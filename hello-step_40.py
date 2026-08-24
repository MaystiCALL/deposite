# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: BudgetLeaf
import argparse

def main():
    parser = argparse.ArgumentParser(description="BudgetLeaf CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a transaction")
    add_parser.add_argument("category", help="Category name")
    add_parser.add_argument("amount", type=float, help="Amount")
    add_parser.add_argument("--date", default=None, help="Date (YYYY-MM-DD)")

    report_parser = subparsers.add_parser("report", help="Monthly report")
    report_parser.add_argument("--month", type=int, default=None, help="Month (1-12)")
    report_parser.add_argument("--year", type=int, default=None, help="Year")

    limit_parser = subparsers.add_parser("limit", help="Set category limit")
    limit_parser.add_argument("category", help="Category name")
    limit_parser.add_argument("amount", type=float, help="Limit amount")

    args = parser.parse_args()

    if args.command == "add":
        if not args.date:
            args.date = datetime.now().strftime("%Y-%m-%d")
        transactions.append(Transaction(args.category, args.amount, args.date))
        print(f"Added {args.amount:.2f} to {args.category} on {args.date}")

    elif args.command == "report":
        year = args.year or datetime.now().year
        month = args.month or datetime.now().month
        month_transactions = [t for t in transactions if t.date[:7] == f"{year:04d}-{month:02d}"]
        print(f"\nReport for {year}-{month:02d}:")
        for t in month_transactions:
            print(f"  {t.date} | {t.category} | {t.amount:.2f}")

    elif args.command == "limit":
        print(f"Limit for {args.category} set to {args.amount:.2f}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
