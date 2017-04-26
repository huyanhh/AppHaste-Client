def record(browser):
    char = 's'
    items = []
    last_item = None
    while char != 'q':
        char = input("\nPress Enter to Record\n"
                     "Enter 'P' to Playback\n"
                     "Enter 'D' to Delete last entry\n"
                     "Enter 'S' to Save all the records\n"
                     "Enter 'L' to Load all the records\n"
                     "Enter 'C' to Clear all the records\n"
                     "Enter 'Q' to Quit the current form\n > ")
        try:
            char = str(char)
            char.lower()
        except ValueError:
            print("Value Error")
            continue
        if char == '\n' or char == '':
            browser.record()
            items = browser.getRecordedElements()
            last_item = items[len(items) - 1]
            print("Element Recorded: {}".format(last_item.output()))
        elif char == 'd':
            if last_item:
                print("Element Deleted: {}".format(last_item.output()))
            err = browser.deleteRecord()
            if err:
                print("Failed to delete or no element is captured to delete")
        elif char == 'p':
            err = browser.playback()
            if err:
                print("Playback completed with Error")
            else:
                print("Playback completed")
        elif char == 's':
            filename = input("Enter the name of the file to save it\n > ")
            if filename and len(filename):
                err = browser.storeRecorder(filename, directory=cur_dir)
            else:
                err = browser.storeRecorder()
            if err:
                print("Failed to store the file")
            else:
                print("File {}.json stored at {}".format(filename, cur_dir))
        elif char == 'l':
            filename = input("Enter the name of the file to load it\n > ")
            if filename and len(filename):
                err = browser.loadRecorder(filename, directory=cur_dir)
            else:
                err = browser.loadRecorder()
            if err:
                print("Failed to load the file")
            else:
                del items[:]
                del last_item
                items = browser.getRecordedElements()
                last_item = items[len(items) - 1]
                print("File {}.json loaded from {}".format(filename, cur_dir))
        elif char == 'c':
            if items and len(items):
                print("Clearing out all the recorded items")
                browser.clearRecorder()
                del items[:]
                if last_item:
                    last_item = None
            else:
                print("Recorded elements is empty")
        elif char == 'q':
            del items[:]
            del last_item
        else:
            continue