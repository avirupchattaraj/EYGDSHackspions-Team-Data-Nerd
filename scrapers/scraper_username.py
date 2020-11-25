import twint

# Configure
c = twint.Config()
c.Username = "EY_India"
c.Limit = 3
c.Store_csv = True
c.Output = "output.csv"

# Run
twint.run.Profile(c)