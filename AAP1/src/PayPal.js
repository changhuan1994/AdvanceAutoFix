import * as React from 'react';
import {StyleSheet, View, TextInput} from 'react-native';
import {Button} from 'react-native-elements';
import {GoogleSignin} from '@react-native-community/google-signin';

/**
 * Name page
 */
export default class PayPal extends React.Component {
  state = {
    isUserSignedIn: false,
    loggedInUser: null,
    checkingSignedInStatus: true,
    isRegistered: true,
    accessToken: '',
    idToken: '',

    first: '',
    last: '111',
    payPal: '',
    userID: '',
  };

  componentDidMount() {
    this.isUserSignedIn();
  }

  render() {
    return (
      <View style={styles.container} style={{top: 50, left: 45}}>
        <TextInput
          placeholder="  PayPal"
          value={this.state.payPal}
          style={styles.textInputStyle}
          onChangeText={input => this.setState({payPal: input})}
        />
        <Button
          buttonStyle={styles.saveAndNextButton}
          titleStyle={{color: 'white', fontSize: 18}}
          type="clear"
          title="Save"
          onPress={() => this.setPayPal()}
        />
      </View>
    );
  }

  getPayPal(loggedInUser) {
    // console.log(loggedInUser);

    let formdata = new FormData();
    formdata.append('user_name', loggedInUser.user.email);
    formdata.append('id_token', loggedInUser.idToken);
    fetch('http://localhost:5000/profile', {
      method: 'POST',
      body: formdata,
    })
      .then(response => response.json())
      .then(responseJson => {
        var name = responseJson.full_name;
        const names = name.split(' ');
        this.setState({
          first: names[0],
          last: names[1],
          payPal: responseJson.paypal_info,
          userID: responseJson.user_id,
        });
      })
      .catch(err => console.log(err));
  }

  setPayPal() {
    const {loggedInUser, first, last, payPal, userID} = this.state;
    let formdata = new FormData();
    formdata.append('user_name', loggedInUser.user.email);
    formdata.append('full_name', first + ' ' + last);
    formdata.append('address', '');
    formdata.append('paypal_info', payPal);
    formdata.append('bio', 'bio');
    formdata.append('user_id', userID);
    formdata.append('id_token', loggedInUser.idToken);
    fetch('http://localhost:5000/profile', {
      method: 'PUT',
      body: formdata,
    })
      .then(response => console.log(response))
      .catch(err => console.log(err.data));
  }

  /**
   * @name isUserSignedIn
   */
  isUserSignedIn = async () => {
    this.setState({
      isUserSignedIn: false,
      checkingSignedInStatus: true,
    });
    const isUserSignedIn = await GoogleSignin.isSignedIn();
    if (isUserSignedIn) {
      await this.getCurrentUserInfo();
    }
    this.setState({
      isUserSignedIn,
      checkingSignedInStatus: false,
    });
  };

  /**
   * @name getCurrentUserInfo
   */
  getCurrentUserInfo = async () => {
    try {
      const loggedInUser = await GoogleSignin.signInSilently();
      const tokens = await GoogleSignin.getTokens();
      this.setState({
        loggedInUser,
        idToken: tokens.idToken,
        accessToken: tokens.accessToken,
      });
      this.getPayPal(loggedInUser);
    } catch (error) {
      this.setState({
        loggedInUser: {},
        idToken: '',
        accessToken: '',
      });
    }
  };
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
  saveAndNextButton: {
    backgroundColor: 'rgb(88,214,141)',
    right: -240,
    top: 30,
    height: 40,
    width: 80,
  },
  textInputStyle: {
    fontSize: 20,
    width: 320,
    height: 50,
    borderWidth: 0,
    borderBottomWidth: 1,
    borderBottomColor: 'rgb(234,236,238)',
  },
});
