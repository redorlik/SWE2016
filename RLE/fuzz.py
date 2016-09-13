from fuzzing.fuzzer import FuzzExecutor

# Files to use as initial input seed.
file_list = ["./features/data/t1.pdf", "./features/data/t3.pdf", "./features/data/t2.jpg"]

# List of applications to test.
apps_under_test = [
        #"/Applications/Adobe Reader 9/Adobe Reader.app/Contents/MacOS/AdobeReader",
        #           "/Applications/PDFpen 6.app/Contents/MacOS/PDFpen 6",
                   "/Applications/Preview.app/Contents/MacOS/Preview",
                   ]

number_of_runs = 130

def test():
    fuzz_executor = FuzzExecutor(apps_under_test, file_list)
    fuzz_executor.run_test(number_of_runs)
    return fuzz_executor.stats

def main():
    stats = test()
    print(stats)
    #print stats #Python 2

if __name__ == '__main__':
    main()
