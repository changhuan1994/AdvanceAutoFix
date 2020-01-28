import * as React from 'react';
import {
  StyleSheet,
  Text,
  View,
  Alert,
  TouchableOpacity,
  Linking,
} from 'react-native';
import {Button} from 'react-native-elements';
import {GoogleSignin} from '@react-native-community/google-signin';

/**
 * The job detail page
 */
export default class JobDetail extends React.Component {
  state = {
    job: this.props.navigation.getParam('job', null),
    status: this.props.navigation.getParam('status', ''),
    buttonName: '',
    loggedInUser: null,
    link: '',
  };

  componentDidMount() {
    this.setButton();
    this.isUserSignedIn();
  }

  render() {
    const {job} = this.state;
    return (
      <View style={{left: 50, top: 80}}>
        <View>
          <Text style={{fontSize: 23}}>Customer Name:</Text>
          <Text style={{fontSize: 22}}>{'\t' + job.customer_name + '\n'}</Text>
          <Text style={{fontSize: 23}}>Location:</Text>
          <Text style={{fontSize: 22}}>{'\t' + job.address + '\n'}</Text>
          <Text style={{fontSize: 23}}>Issue:</Text>
          <Text style={{fontSize: 22}}>{'\t' + job.job_type_name + '\n'}</Text>
          <Text style={{fontSize: 23}}>Details:</Text>
          <Text style={{fontSize: 22}}>{'\t' + job.details + '\n'}</Text>
          <TouchableOpacity
            onPress={() => {
              Linking.openURL(this.state.link);
            }}>
            <Text
              style={{
                top: 10,
                left: 25,
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
        <Button
          buttonStyle={{
            backgroundColor: 'rgb(88,214,141)',
            height: 40,
            width: 80,
            top: 30,
            left: 200,
          }}
          titleStyle={{fontSize: 18, color: 'white'}}
          type="clear"
          title={this.state.buttonName}
          onPress={() => this.acceptOrCancel()}
        />
        {this.state.buttonName === 'Cancel' && (
          <Button
            buttonStyle={{
              backgroundColor: 'rgb(88,214,141)',
              height: 40,
              width: 80,
              bottom: 10,
              left: 40,
            }}
            titleStyle={{fontSize: 18, color: 'white'}}
            type="clear"
            title={'Start'}
            onPress={() => this.startJob()}
          />
        )}
      </View>
    );
  }

  startJob() {}

  setUsers(loggedInUser) {
    this.setState({loggedInUser: loggedInUser});
    let formdata = new FormData();
    formdata.append('user_name', loggedInUser.user.email);
    formdata.append('id_token', loggedInUser.idToken);
    fetch('http://localhost:5000/job/vediolink', {
      method: 'POST',
      body: formdata,
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status === undefined) {
          for (let i = 0; i < responseJson.length; i++) {
            if (responseJson[i][0] === this.state.job.job_type_id) {
              // this.setState({link: responseJson[i][2]});
              this.setState({link: 'https://video.advanceautoparts.com/'});
              break;
            }
          }
        }
        // console.log(this.state.link);
      })
      .catch(err => console.log(err));
  }

  setButton() {
    if (this.state.status === 'unbooked') {
      this.setState({buttonName: 'Accept'});
    } else if (this.state.status === 'booked') {
      this.setState({buttonName: 'Cancel'});
    } else {
      Alert.alert('Error', 'This job is processing');
    }
  }

  acceptOrCancel() {
    var apiCall = '';
    if (this.state.status === 'unbooked') {
      apiCall = 'http://localhost:5000/job/book';
    } else if (this.state.status === 'booked') {
      apiCall = 'http://localhost:5000/job/unbook';
    }
    let formdata = new FormData();
    formdata.append('user_name', this.state.loggedInUser.user.email);
    formdata.append('id_token', this.state.loggedInUser.idToken);
    formdata.append('job_id', this.state.job.job_id.toString());
    if (this.state.status === 'unbooked') {
      formdata.append('store_id', '1');
    }
    fetch(apiCall, {
      method: 'POST',
      body: formdata,
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status !== undefined) {
          this.props.navigation.goBack();
        }
      })
      .catch(err => console.log(err));
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
        loggedInUser: loggedInUser,
        idToken: tokens.idToken,
        accessToken: tokens.accessToken,
      });
      this.setUsers(loggedInUser);
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
    backgroundColor: '#fff',
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
