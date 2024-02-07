
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # Specify your transformation logic here
    
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data = data.rename(columns = {'VendorID':'vendor_id'})
    vendor_id_value = data['vendor_id'].unique().tolist()
    
    print("valid vendor id: ", vendor_id_value) 
    print("Rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    print("Rows with zero trip_distance:", data['trip_distance'].isin([0]).sum())
    
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    valid_vendor_ids = [1,2]  # Replace with your actual valid vendor IDs

    assert output['vendor_id'].isin(valid_vendor_ids).all(), 'There are invalid vendor ids'
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passenger'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'
