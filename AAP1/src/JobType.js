import * as React from 'react';
import {StyleSheet, Text, View, Button} from 'react-native';
import Select from 'react-native-select-plus';

/**
 * the job type page
 */
export default class JobType extends React.Component {
  state = {
    item: null,
    items: [
      {key: 1, label: 'aaa'},
      {key: 2, label: 'Red Apples'},
      {key: 3, label: 'Cherries'},
      {key: 4, label: 'Cranberries'},
      {key: 5, label: 'Pink Grapefruit'},
      {key: 6, label: 'Raspberries'},
      {key: 7, label: 'Vegetables'},
      {key: 8, label: 'Beets'},
      {key: 9, label: 'Red Peppers'},
      {key: 10, label: 'Radishes'},
      {key: 11, label: 'Radicchio'},
      {key: 12, label: 'Red Onions'},
      {key: 13, label: 'Red Potatoes'},
      {key: 14, label: 'Rhubarb'},
      {key: 15, label: 'Tomatoes'},
    ],
  };
  onSelectedItemsChange = (key, value) => {
    this.setState({item: {key: key, value: value}});
  };
  onSubmit() {
    // api function call
  }

  render() {
    const {items} = this.state;
    return (
      <View style={styles.container}>
        <Select
          data={items}
          width={250}
          placeholder="Select a value ..."
          onSelect={this.onSelectedItemsChange.bind(this)}
          search={true}
        />
        <Button
          buttonStyle={styles.saveAndNextButton}
          titleStyle={{color: 'white', fontSize: 18}}
          type="clear"
          title="Save"
          onPress={() => this.onSubmit()}
        />
      </View>
    );
  }
}

/**
 * Styles for the whole app
 */
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    color: 'black',
    fontWeight: 'bold',
    fontSize: 35,
    bottom: 120,
    left: 0,
  },
  subtitle: {
    color: 'black',
    fontSize: 20,
    bottom: 110,
    left: 100,
  },
  loginScreenButton: {
    marginRight: 40,
    marginLeft: 40,
    marginTop: 10,
    paddingTop: 10,
    paddingBottom: 10,
    backgroundColor: '#1E6738',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#fff',
  },
  textInputStyle: {
    fontSize: 20,
    width: 320,
    height: 50,
    borderWidth: 0,
    borderBottomWidth: 1,
    borderBottomColor: 'rgb(234,236,238)',
  },
  buttonStyle: {
    backgroundColor: 'rgb(234,236,238)',
    height: 60,
    width: 450,
  },
  saveAndNextButton: {
    backgroundColor: 'rgb(88,214,141)',
    right: -240,
    top: 30,
    height: 40,
    width: 80,
  },
  titleStyle: {
    color: 'rgb(128,139,150)',
    fontSize: 20,
  },
  checkBoxContainer: {
    backgroundColor: 'white',
    borderWidth: 0,
  },
});
