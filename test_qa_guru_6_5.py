import os

from selene import browser, have, be

def test_homework1 (browser_open):
    browser.open('/automation-practice-form')

    #Заполняем форму
    browser.element('#firstName').type("Damir")
    browser.element('#lastName').type("Nabiullin")
    browser.element('#userEmail').type("NabiullinDM@mail.ru")
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type("9375234688")
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().type("1985").click()
    browser.element('[class="react-datepicker__month-select"]').click().type("December").click()
    browser.element('[aria-label="Choose Wednesday, December 4th, 1985"]').click()
    browser.element('#subjectsInput').type('economics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("image/bd.png"))
    browser.element('#currentAddress').type("Glushko 31")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#submit').should(be.visible).press_enter()

#Проверяем форму
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive .table thead tr th')[1].should(have.text('Values'))
    browser.all('.table-responsive .table thead tr th')[0].should(have.text('Label'))
    browser.all('.table-responsive .table tbody tr')[0].should(have.text('Damir Nabiullin'))
    browser.all('.table-responsive .table tbody tr')[1].should(have.text('NabiullinDM@mail.ru'))
    browser.all('.table-responsive .table tbody tr')[2].should(have.text('Male'))
    browser.all('.table-responsive .table tbody tr')[3].should(have.text('9375234688'))
    browser.all('.table-responsive .table tbody tr')[4].should(have.text('04 December,1985'))
    browser.all('.table-responsive .table tbody tr')[5].should(have.text('Economics'))
    browser.all('.table-responsive .table tbody tr')[6].should(have.text('Sports'))
    browser.all('.table-responsive .table tbody tr')[7].should(have.text('bd.png'))
    browser.all('.table-responsive .table tbody tr')[8].should(have.text('Glushko 31'))
    browser.all('.table-responsive .table tbody tr')[9].should(have.text('NCR Gurgaon'))