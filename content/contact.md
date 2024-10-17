Title: Contact
Date: 2010-12-03 10:20
######################


<form class="contact-message-contact-form contact-message-form contact-form" data-user-info-from-browser="" data-drupal-selector="contact-message-contact-form" action="https://formspree.io/f/mrbggrjq" method="post" id="contact-message-contact-form" accept-charset="UTF-8" data-once="form-updated user-info-from-browser" data-drupal-form-fields="edit-name,edit-mail,edit-subject-0-value,edit-message-0-value,edit-submit">
  <div class="js-form-item form-item js-form-type-textfield form-type-textfield js-form-item-name form-item-name">
      <label for="edit-name" class="js-form-required form-required">Your name<span class="visually-hidden"> (Required)</span></label>
        <input data-drupal-selector="edit-name" type="text" id="edit-name" name="name" value="" size="60" maxlength="255" class="form-text required" required="required" aria-required="true">

        </div>
<input data-drupal-selector="form-ktttp8c6rzj-6-hbslqp6gb5fg7u8orbedceovql8hc" type="hidden" name="form_build_id" value="form-KtTtP8c6rZj-6_hBslQP6gb5fG7U8OrBedCEOvql8hc">
<input data-drupal-selector="edit-contact-message-contact-form" type="hidden" name="form_id" value="contact_message_contact_form">
<div class="js-form-item form-item js-form-type-email form-type-email js-form-item-mail form-item-mail">
      <label for="edit-mail" class="js-form-required form-required">Your email address<span class="visually-hidden"> (Required)</span></label>
        <input data-drupal-selector="edit-mail" type="email" id="edit-mail" name="mail" value="" size="60" maxlength="254" class="form-email required" required="required" aria-required="true">

        </div>
<div class="field--type-string field--name-subject field--widget-string-textfield js-form-wrapper form-wrapper" data-drupal-selector="edit-subject-wrapper" id="edit-subject-wrapper">      <div class="js-form-item form-item js-form-type-textfield form-type-textfield js-form-item-subject-0-value form-item-subject-0-value">
      <label for="edit-subject-0-value" class="js-form-required form-required">Subject<span class="visually-hidden"> (Required)</span></label>
        <input class="js-text-full text-full form-text required" data-drupal-selector="edit-subject-0-value" type="text" id="edit-subject-0-value" name="subject[0][value]" value="" size="60" maxlength="100" placeholder="" required="required" aria-required="true">

        </div>

  </div>
<div class="field--type-language field--name-langcode field--widget-language-select js-form-wrapper form-wrapper" data-drupal-selector="edit-langcode-wrapper" id="edit-langcode-wrapper">      
  </div>
<div class="field--type-string-long field--name-message field--widget-string-textarea js-form-wrapper form-wrapper" data-drupal-selector="edit-message-wrapper" id="edit-message-wrapper">      <div class="js-form-item form-item js-form-type-textarea form-type-textarea js-form-item-message-0-value form-item-message-0-value">
      <label for="edit-message-0-value" class="js-form-required form-required">Message<span class="visually-hidden"> (Required)</span></label>
        <div class="form-textarea-wrapper">
  <textarea class="js-text-full text-full form-textarea required resize-vertical" data-drupal-selector="edit-message-0-value" id="edit-message-0-value" name="message[0][value]" rows="12" cols="60" placeholder="" required="required" aria-required="true"></textarea>
</div>

        </div>

  </div>
<div data-drupal-selector="edit-actions" class="form-actions js-form-wrapper form-wrapper" id="edit-actions"><input data-drupal-selector="edit-submit" type="submit" id="edit-submit" name="op" value="Send message" class="button button--primary js-form-submit form-submit">
</div>

</form>

<script>
document.getElementById("contact-form").addEventListener("submit", function(event) {
    // Prevent form submission
    event.preventDefault();

    // Get form fields
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Check if fields are empty
    if (!name || !email || !message) {
        alert("All fields are required!");
        return;
    }

    // If validation passes, submit the form
    this.submit();
});
</script>
