from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file...")

    def process_data(self):
        print("Processing CSV data...")

    def save_data(self):
        print("Saving processed data to CSV file.")


class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from JSON file...")

    def process_data(self):
        print("Processing JSON data...")

    def save_data(self):
        print("Saving processed data to JSON file.")


print("> CVS related:")
csv_processor = CSVDataProcessor()
csv_processor.process()

print("> JSON related:")
json_processor = JSONDataProcessor()
json_processor.process()
