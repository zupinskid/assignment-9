from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """A GUI-based tax calculator."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for gross income
        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0,
                                              row=0,
                                              column=1,
                                              precision=2)

        # Label and field for number of dependents
        self.addLabel(text="Dependents", row=1, column=0)
        self.dependentsField = self.addIntegerField(value=0,
                                                    row=1,
                                                    column=1)

        # Command button
        self.addButton(text="Compute",
                       row=2,
                       column=0,
                       columnspan=2,
                       command=self.computeTax)

        # Label and output field for total tax
        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value=0.0,
                                           row=3,
                                           column=1,
                                           precision=2)

    def computeTax(self):
        """Gets the input values, computes the tax, and displays it."""
        grossIncome = self.incomeField.getNumber()
        dependents = self.dependentsField.getNumber()

        standardDeduction = 10000.0
        dependentDeduction = 3000.0
        taxRate = 0.20

        taxableIncome = grossIncome - standardDeduction - (dependents * dependentDeduction)

        if taxableIncome < 0:
            taxableIncome = 0.0

        tax = taxableIncome * taxRate
        self.taxField.setNumber(tax)


def main():
    """Instantiates and pops up the window."""
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
