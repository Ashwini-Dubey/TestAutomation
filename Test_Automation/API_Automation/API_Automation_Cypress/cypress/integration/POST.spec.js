/// <reference types="cypress" />

describe ('API Automation - POST Method', () =>
{
    let accessToken = '0dca8de44b53f262d13eb6e8d85f82c75eb345ff8771b7072959b57b6a81ccd7'
    const uid = () => Cypress._.random(0,1e6)
    const id = uid()
    const email = `cyapitest${id}@yopmail.com`
    
        it('User Creation Test', () => {
            cy.request({
                method : 'POST',
                url : 'https://gorest.co.in/public/v1/users',
                headers : {
                    'authorization' : 'Bearer ' + accessToken
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