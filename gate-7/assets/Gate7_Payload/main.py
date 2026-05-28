import sys

def main():
    try:
        import upload_core
        upload_core.boot()
    except ImportError as e:
        print("FATAL: Mind Upload Protocol Core Corrupted.")
        print(f"Diagnostics: {e}")
        print("System halted. The transfer script lacks foundational signatures.")
        sys.exit(1)
    except Exception as e:
        print(f"Unknown neural fault: {e}")

if __name__ == "__main__":
    main()