#percent error wrt to first argument with default accuracy of 2 decimal places
def err_percent(baseline, final, acc = 2):
    reduction = round(((final - baseline)/ baseline) * 100, acc)
    print('Error percentage change : {} %'.format(reduction))
