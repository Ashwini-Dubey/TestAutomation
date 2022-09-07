/// <reference types="cypress" />

let testData;

describe ('API Automation - POST Method', () =>
{
    const uid = () => Cypress._.random(0,1e6)
    const id = uid()
    const email = `cyapitest${id}@yopmail.com`

    before(() => {
        cy.fixture('user_testdata/user_testdata').then((data) =>
        {
            cy.log(data)
            testData = data
        })
    })
    
    it('Test to verify that user is created successfully with all the valid request data.', () => {
        cy.request({
            method : 'POST',
            url : 'https://gorest.co.in/public/v1/users',
            headers : {
                'authorization' : 'Bearer ' + testData.accessToken
            },
            body : {
                "name" : "API Tester",
                "gender" : "male",
                "email" : email,
                "status" : "active"
            }
        })
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(201)
            expect(Response.body.data.id).is.exist
            expect(Response.body.data.name).to.eq('API Tester')
            expect(Response.body.data.gender).to.eq('male')
            expect(Response.body.data.email).to.eq(email)
            })
    })  

})

describe('API Automation - POST Method with fixture' , () => 
{
    const uid = () => Cypress._.random(0,1e6)
    const id = uid()
    const email = `cyapitest${id}@yopmail.com`

    before(() => {
        cy.fixture('user_testdata/user_testdata').then((data) =>
        {
            cy.log(data)
            testData = data
        })
    })
    it('Test to verify that user is created successfully with all the valid request data from fixtures file.', () => {
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
            .should((Response) => {
            cy.log(JSON.stringify(Response.body))
            expect(Response.status).to.eq(201)
            expect(Response.body.data.id).is.exist
            expect(Response.body.data.name).to.eq('API Tester')
            expect(Response.body.data.gender).to.eq('male')
            expect(Response.body.data.email).to.eq(email)
            })
    })
})