import builtwith
import whois

#tech = builtwith.parse('https://earthquake.usgs.gov/earthquakes/map/?extent=-89.58992,-357.1875&extent=89.58992,717.1875&range=search&listOnlyShown=true&baseLayer=terrain&timeZone=utc&search=%7B%22name%22:%22Search%20Results%22,%22params%22:%7B%22starttime%22:%221900-01-01%2000:00:00%22,%22minmagnitude%22:7,%22orderby%22:%22time%22%7D%7D')
tech = builtwith.parse('https://earthquake.usgs.gov/earthquakes/map/')
print(tech)

print(whois.whois('https://earthquake.usgs.gov/earthquakes/map/'))
