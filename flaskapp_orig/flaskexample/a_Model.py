def ModelIt(fromUser  = 'Default', tweets = []):
  numtweets = len(tweets)
  print 'The number of tweets are %i' % numtweets
  result = numtweets 
  if fromUser != 'Default':
    return result
  else:
    return 'check your input'
