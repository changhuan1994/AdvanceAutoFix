import * as React from 'react';
import {StyleSheet, View, Alert, TextInput, Text} from 'react-native';
import {Button} from 'react-native-elements';
import {GoogleSignin} from '@react-native-community/google-signin';
import Geolocation from 'react-native-geolocation-service';
import Slider from '@react-native-community/slider';
/**
 * The location and distance page
 */
export default class LocationAndDistance extends React.Component {
  static navigationOptions = {
    title: 'Location & Distance',
  };

  constructor(props) {
    super(props);
    this.state = {
      value: 0,
      longitude: '',
      latitude: '',
    };
  }

  componentDidMount() {
    this.getAddress();
  }

  render() {
    return (
      <View
        style={{
          top: -230,
          left: 40,
          width: 330,
          flex: 1,
          alignItems: 'stretch',
          justifyContent: 'center',
        }}>
        <Text style={{fontSize: 20}}>{'Coordinate'}</Text>
        <View style={{flexDirection: 'row', left: 50, top: 5}}>
          <TextInput
            placeholder="  Latitude"
            value={this.state.latitude}
            style={styles.textInputStyle}
            keyboardType={'numeric'}
            onChangeText={input => this.setState({latitude: input})}
          />
          <Text style={{top: 15, fontSize: 25}}> {',\t'}</Text>
          <TextInput
            placeholder="  Longitude"
            value={this.state.longitude}
            style={styles.textInputStyle}
            keyboardType={'numeric'}
            onChangeText={input => this.setState({longitude: input})}
          />
        </View>
        <Text style={{fontSize: 20}}>{'\nRange'}</Text>
        <Slider
          style={{top: 10, width: 240, height: 40, left: 35}}
          value={this.state.value}
          minimumValue={0}
          maximumValue={100}
          minimumTrackTintColor="green"
          maximumTrackTintColor="grey"
          onValueChange={input => this.setState({value: input})}
        />
        <Text style={{top: 5, left: 230}}>
          {parseFloat(this.state.value)
            .toFixed(2)
            .toString() + ' miles'}
        </Text>
        <View style={{flexDirection: 'row', bottom: 20, left: 40}}>
          <Button
            buttonStyle={styles.saveAndNextButton}
            titleStyle={{color: 'white', fontSize: 18}}
            type="clear"
            title="Reset"
            onPress={() => this.reset()}
          />
          <Text>{'\t\t\t'}</Text>
          <Button
            buttonStyle={styles.saveAndNextButton}
            titleStyle={{color: 'white', fontSize: 18}}
            type="clear"
            title="Save"
            onPress={() => {}}
          />
        </View>
      </View>
    );
  }
  z;

  reset() {
    this.getAddress();
    this.setState({value: 0});
  }

  // setValue(input) {
  //   var temp = parseFloat(input).toFixed(2);
  //   var value = temp.toString();
  //   this.setState({value: value});
  // }

  getAddress() {
    Geolocation.getCurrentPosition(
      position => {
        // const location = JSON.stringify(position);
        this.setState({
          latitude: position.coords.latitude.toFixed(3).toString(),
          longitude: position.coords.longitude.toFixed(3).toString(),
        });
      },
      error => Alert.alert(error.message),
      {enableHighAccuracy: true, timeout: 5000, maximumAge: 10000},
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
    width: 100,
    height: 40,
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
    top: 100,
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
