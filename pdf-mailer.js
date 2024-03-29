const nodemailer = require("nodemailer");
const dotenv = require("dotenv");
const receivers = require("./receivers.json");

dotenv.config();
const transport = nodemailer.createTransport({
    service: "gmail",
    auth:{
        user: process.env.USER, //your Email address
        pass: process.env.PASSWD    //password generated for the third party app in gmail(ex for nodemailer)
    }
})

// var cnt = 10;
// const chunkSize = 5;
// for (let i = 0; i < receivers.length; i += chunkSize) {
//     const chunk = receivers.slice(i, i + chunkSize);
// 	// var delayInMilliseconds = 10000;
//     chunk.forEach((element, index)=> {
//         // console.log(element);
//         if(element.email != ""){
//             setTimeout(()=>{
//                 Send(element);
//                 console.log(index);
//             }, 4000);
//         }
//     });
// }

const Send = (receiver) => {
    const options = {
        from: process.env.USER,
        to: receiver.EMAIL,
        subject: "Prodigy Participation Certificate",
        text: "Hello, "+receiver.NAME+",\nGreetings from ACM-CEG! \n\n\tA hearty congratulations for securing "+ receiver.PRIZE +" in "+ receiver.EVENT +" ! We hope you enjoyed and had fun participating. \nWe would be elated to have you next year too for our next edition of Prodigy. Thank you for your support and participation towards making this event a grand success \n\n\tKindly let us know your feedback and suggestions to make Prodigy better in the future.\nFeedback form: https://forms.gle/zWhZ6dQHFW3TXE9j6 \n\n\nWarm regards,\nACM-CEG.",
        attachments : [
			{
                filename: receiver.NAME+'_'+receiver.ID+'.pdf',
                path: __dirname+'/E-certificates/'+ receiver.NAME+'_'+receiver.ID+'.pdf'
			}
		]
    };
    // console.log(options);
    
    transport.sendMail(options, (err, info)=> {
        if(err){
            console.log(err);
        } else {
            console.log(`Mail sent to ${receiver.NAME} with Id ${receiver.ID}`);
            cnt += 1;
        }
    });
    // console.log(`Sending Email to ${receiver.name} with Id ${receiver.id}`);
}

// Send();
receivers.forEach((element, index)=> {
    if(element.EMAIL != ""){
        if(element.ID > 0 && element.ID <= 37){
            setTimeout(()=>{
                Send(element);
            }, index * 5000);
        }
    }
});

// console.log("Successfully completed");
// console.log(`Total Email sent: ${cnt}`);