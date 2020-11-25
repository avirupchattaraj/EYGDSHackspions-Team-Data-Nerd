import twint

# Configure
c = twint.Config()
c.Username = "realDonaldTrump"
c.Search = "great"
c.Limit = 3
c.Store_csv = True
c.Output = "output.csv"

# Run
twint.run.Search(c)