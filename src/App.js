import React, { Component } from "react";
import "./App.css";
import "./bootstrap/css/bootstrap.min.css";

export default class App extends Component {
  constructor(props) {
    super(props);

    this.addActiveClass = this.addActiveClass.bind(this);
  }
  addActiveClass() {}

  addrequest(e) {
    if (
      this.inputElement.value !== "" &&
      this.name.value !== "" &&
      this.address.value !== "" &&
      this.number.value
    ) {
      var newRequest = {
        text: this.inputElement.value,
        key: Date.now()
      };

      this.setState(prevState => {
        return {
          fridgeRepairRequests: prevState.fridgeRepairRequests.concat(
            newRequest
          )
        };
      });
    }
    var xhr = new XMLHttpRequest();
    xhr.open(
      "GET",
      "https://api.telegram.org/bot667797791:AAEO-pOPrPH3sDPZTNUKnwR7Wt8RJrIDvj4/sendMessage?chat_id=855636692&parse_mode=html&text=Сообщение с сайта:" +
        "%0AИмя: " +
        this.name.value +
        "%0AНомер телефона: " +
        this.number.value +
        "%0AАдрес: " +
        this.address.value +
        "%0AТип услуги: " +
        this.type.value +
        "%0AОписание: " +
        newRequest.text,
      true
    );
    xhr.send();

    this.inputElement.value = "";

    this.name.value = "";

    this.address.value = "";

    this.number.value = "";

    console.log(this.state.fridgeRepairRequests);

    e.preventDefault();
  }

  deleterequest(key) {
    var filteredRequests = this.state.fridgeRepairRequests.filter(function(
      request
    ) {
      return request.key !== key;
    });

    this.setState({
      fridgeRepairRequests: filteredRequests
    });
  }

  render() {
    return (
      <div className="App">
        <div className="main">
          <div className="choose">
            <form className="form container">
              <div className="header row">
                <div className="col">Choose Profile</div>
              </div>
              <div className="row">
                <div className="col">
                  <input placeholder="Link: " />
                </div>
              </div>
              <div className="row">
                <div className="col ">
                  <button className="vk">VK</button>
                </div>
                <div className="col">
                  <button className="instagram">Instagram</button>
                </div>
                <div className="col">
                  <button className="facebook">Facebook</button>
                </div>
              </div>
              <div className="row">
                <div className="col">
                  <button className="go" type="submit">
                    Go
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
