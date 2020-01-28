import * as React from 'react';
import { 
  StyleSheet,
  View, 
  TextInput,
} from 'react-native';
import { Button } from 'react-native-elements';

/**
 * Phone number page
 */
export default class PhoneNumber extends React.Component {
  render() {
    return (
      <View style={styles.container} style={{top: 50, left: 45}}>
        <TextInput 
          placeholder='  Phone Number'
          style={styles.textInputStyle}
          onChangeText={(phoneNumber) => {}}
          keyboardType={'numeric'}
          />
        <Button 
          buttonStyle={styles.saveAndNextButton}
          titleStyle={{color:'white', fontSize: 18}}
          type='clear'
          title='Save'
          onPress={() => {}}
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
  loginScreenButton:{
    marginRight:40,
    marginLeft:40,
    marginTop:10,
    paddingTop:10,
    paddingBottom:10,
    backgroundColor:'#1E6738',
    borderRadius:10,
    borderWidth: 1,
    borderColor: '#fff'
  },
  textInputStyle:{
    fontSize: 20,
    width: 320, 
    height: 50, 
    borderWidth: 0,
    borderBottomWidth: 1,
    borderBottomColor: 'rgb(234,236,238)'
  },
  buttonStyle: {
    backgroundColor:'rgb(234,236,238)',
    height: 60,
    width: 450,
  },
  saveAndNextButton: {
    backgroundColor:'rgb(88,214,141)',
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
  }
});
