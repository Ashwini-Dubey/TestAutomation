/*
Request Chaining for POST , GET , PUT & DELETE API Call
*/
/// <reference types="cypress" />

let testData;
const payload = require('../fixtures/user_testdata/user_testdata')

describe('API Automation - POST Method with fixture' , () => 
{
    const uid = () => Cypress._.random(0,1e6)
    const id = uid()
    const email = `cyapitest${id}@yopmail.com`

    //Fetching the payload data fom the fixture file
    before(() => {
        cy.fixture('user_testdata/user_testdata').then((data) =>
        {
            cy.log(data)
            testData = data
        })
    })

    // API Call Test Suite
    it('Test to verify that user is created successfully with all the valid request data from fixtures file.', () => {
        
        //Request Call for POST Method
        cy.request({
            method : 'POST',
            url : 'https://gorest.co.in/public/v1/users',
            headers : {
                'authorization' : 'Bearer ' + testData.accessToken
            },
            body : {
                "name" : testData.name,
                "gender" : testData.gender,
                "email" : email,
                "status" : testData.status
            }
        })
        //Fetching the response for the GET Request
        .then((Response) => {
            cy.log(JSON.stringify(Response))
            expect(Response.status).to.eq(201)
            expect(Response.body.data.id).is.exist
            expect(Response.body.data.name).to.eq('API Tester')
            expect(Response.body.data.gender).to.eq('male')
            expect(Response.body.data.email).to.eq(email)
            })
        //Capturing the User ID from the GET Request
       .then((Response) =>{
                    const userId = Response.body.data.id
                    cy.log(userId)

                //Request Call for GET Method
                
                cy.request({
                    method : 'GET',
                    url : 'https://gorest.co.in/public/v1/users/' + userId,
                    headers : {
                        'authorization' : 'Bearer ' + payload.accessToken
                    }
                })
                .then((Response) => {
                    expect(Response.status).to.eq(200)
                    expect(Response.body.data).has.property('email',email)
                    expect(Response.body.data).has.property('id',userId)
                
                })

                //Request Call for PUT Method
                cy.request({
                    method : 'PUT',
                    url : 'https://gorest.co.in/public/v1/users/' +userId,
                    headers : {
                        'authorization' : 'Bearer ' + testData.accessToken
                    },
                    body : {
                        "name" : testData.name,
                        "email" : email,
                        "status" : testData.status
                    }
                })
                .then((Response) => {
                    cy.log(JSON.stringify(Response.body))
                    expect(Response.status).to.eq(200)
                    expect(Response.body.data.id).is.exist
                    expect(Response.body.data.name).to.eq('API Tester')
                    expect(Response.body.data.email).to.eq(email)
                })

                //Request Call for DELETE Method
                cy.request({
                    method : 'DELETE',
                    url : 'https://gorest.co.in/public/v2/users/' +userId,
                    headers : {
                        'authorization' : 'Bearer ' + testData.accessToken
                    }
                })
                .then((Response) => {
                    cy.log(JSON.stringify(Response.body))
                    expect(Response.status).to.eq(204)
                })
                
            })
    })
})