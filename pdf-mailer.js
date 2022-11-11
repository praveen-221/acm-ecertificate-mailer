const nodemailer = require("nodemailer");
const dotenv = require("dotenv");
const receivers = require("./receivers.json");

dotenv.config();
const transport = nodemailer.createTransport({
    service: "gmail",
    auth:{
        user: process.env.USER,
        // pass: "*********"
        pass: process.env.PASSWD
    }
})

var cnt = 1;

const Send = (receiver) => {
    const options = {
        from: "test_mail@gmail.com",
        to: receiver.email,
        subject: "Hello from space",
        text: "     Hi "+ receiver.name +", If you see this mail then nodemailer works perfectly.\nJust playing buddy :):" + '\n' +
        "   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    };
    // console.log(options);
    
    console.log(`Sending Email: ${cnt}`);
    
    transport.sendMail(options, (err, info)=> {
        if(err){
            console.log(err);
        } else {
            console.log("Success: ", info);
            cnt += 1;
        }
    });
}

receivers.forEach((element, index)=> {
    if(element.email != ""){
        setTimeout(()=>{
            Send(element);
            console.log(index);
        }, element.id * 5000);
    }
});