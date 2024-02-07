if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd



@transformer
def transform(data, *args, **kwargs):


    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_date']).dt.date #was Assigned as category

    print(data.info())

    data.columns = (data.columns
                    .str.replace(" ","_")
                    .str.lower()
    )

    return data



# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
