import * as React from 'react';
import {StyleSheet, View, FlatList, Alert} from 'react-native';
import {Button} from 'react-native-elements';

/**
 * Job List page
 */
export default class JobList extends React.Component {
  state = {
    jobList: [],
    loggedInUser: this.props.navigation.getParam('loggedInUser', null),
    preference: this.props.navigation.getParam('preference', null),
    distance: this.props.navigation.getParam('distance', null),
    longitude: this.props.navigation.getParam('longitude', null),
    latitude: this.props.navigation.getParam('latitude', null),
  };

  componentDidMount() {
    this.getJobList();
  }

  render() {
    return (
      <View style={styles.container}>
        <FlatList
          data={this.state.jobList}
          keyExtractor={(item, index) => index.toString()}
          renderItem={({item}) => (
            <View>
              <Button
                buttonStyle={styles.buttonStyle}
                titleStyle={styles.titleStyle}
                style={styles.fullWidthButton}
                title={item.customer_name + "'s order"}
                onPress={() => this.jobDetail(item)}
              />
            </View>
          )}
        />
      </View>
    );
  }

  getJobList() {
    let formdata = new FormData();
    formdata.append('user_name', this.state.loggedInUser.user.email);
    formdata.append('id_token', this.state.loggedInUser.idToken);
    formdata.append('logitude', this.state.longitude);
    formdata.append('latitude', this.state.latitude);
    formdata.append('distance', this.state.distance);
    formdata.append('preference', this.state.preference);
    fetch('http://localhost:5000/job/distance', {
      method: 'POST',
      body: formdata,
    })
      .then(response => response.json())
      .then(responseJson => {
        if (responseJson.status === undefined) {
          var list = [];
          for (let i = 0; i < responseJson.length; i++) {
            var temp = responseJson[i];
            var job = {
              job_id: temp.job_id,
              job_type_id: temp.job_type_id,
              address: temp.address,
              details: temp.details,
              cus_id: temp.cus_id,
              customer_name: temp.customer_name,
              job_type_name: temp.job_type_name,
            };
            list.push(job);
          }
          this.setState({jobList: list});
        } else {
          Alert.alert('Error', responseJson.response);
        }
      })
      .catch(err => console.log(err));
  }

  jobDetail(job) {
    this.props.navigation.navigate('JobDetail', {
      job: job,
      status: 'unbooked',
    });
    // console.log(job);
  }
}

/**
 * Styles for the whole app
 */
const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  fullWidthButton: {
    backgroundColor: 'grey',
    height: 50,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'stretch',
  },
  buttonStyle: {
    backgroundColor: 'rgb(234,236,238)',
    height: 60,
    width: 450,
  },
  titleStyle: {
    color: 'rgb(128,139,150)',
    fontSize: 20,
  },
});
