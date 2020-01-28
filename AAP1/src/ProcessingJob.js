import * as React from 'react';
import {StyleSheet, Text, View, Linking, TouchableOpacity} from 'react-native';
import {Button} from 'react-native-elements';
import openMap from 'react-native-open-maps';

/**
 * The Processing job page
 */
export default class ProcessingJob extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      make: '',
      model: '',
      location: '',
      issue: '',
      date: '',
      time: '',
      status: '',
    };
  }
  render() {
    return (
      <View>
        <View style={{left: 70, top: 100}}>
          <View>
            <Text style={{fontSize: 20}}> Name: Huan Chang </Text>
            <Text style={{fontSize: 20}}> Make: Land Rover </Text>
            <Text style={{fontSize: 20}}> Model: Range Rover Velar </Text>
            <TouchableOpacity
              onPress={() => {
                openMap({
                  // latitude: 35.779591,
                  // longitude: -78.638176,
                  navigate_mode: 'preview',
                  travelType: 'drive',
                  start: '35.779591, -78.638176',
                  end: 'RDU',
                });
              }}>
              <Text style={{fontSize: 20}}> Location: EB2 </Text>
            </TouchableOpacity>
            <Text style={{fontSize: 20}}> Issue: Replace front wiper </Text>
            <Text style={{fontSize: 20}}> Time: 2:00pm to 5:00pm </Text>
            <Text style={{fontSize: 20}}> Date: 10/22/2019 </Text>
            <Text style={{fontSize: 20}}> Status: Tool(s) picking up </Text>
          </View>
        </View>
        <View style={{top: 120}}>
          <TouchableOpacity
            onPress={() => {
              Linking.openURL('telprompt:9845008050');
            }}>
            <Text
              style={{
                left: 80,
                textAlign: 'left',
                fontSize: 14,
                color: '#48b2f6',
                textDecorationLine: 'underline',
              }}>
              {' '}
              Contact Owner?{' '}
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => {
              Linking.openURL('https://video.advanceautoparts.com/');
            }}>
            <Text
              style={{
                left: 80,
                textAlign: 'left',
                fontSize: 14,
                color: '#48b2f6',
                textDecorationLine: 'underline',
              }}>
              {' '}
              Have trouble on fixing the car?{' '}
            </Text>
          </TouchableOpacity>
        </View>
        <View style={{flexDirection: 'row'}}>
          <Button
            buttonStyle={{
              backgroundColor: 'rgb(88,214,141)',
              height: 40,
              width: 140,
              top: 200,
              left: 60,
            }}
            titleStyle={{fontSize: 18, color: 'white'}}
            type="clear"
            title="Nearby AAPs"
            onPress={() => {}}
          />
          <Button
            buttonStyle={{
              backgroundColor: 'rgb(88,214,141)',
              height: 40,
              width: 80,
              top: 200,
              left: 120,
            }}
            titleStyle={{fontSize: 18, color: 'white'}}
            type="clear"
            title="Next"
            onPress={() => {}}
          />
        </View>
      </View>
    );
  }
}

/**
 * Styles for the whole app
 */
const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
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
});
