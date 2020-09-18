def track_error(history, track_metric = 'error'):
  # keep a global variable to keep track referring to the same name
  global tracking_df
  train_err = history[track_metric]
  val_err = history['val_' + track_metric]
  row = dict(train_error = train_err, val_error = val_err)
  row_df = pd.DataFrame(row, index = [0])
  tracking_df = pd.concat([tracking_df, entry_df])
  tracking_df.reset_index(drop =True, inplace = True)
  print('History saved')