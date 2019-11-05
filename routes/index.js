const express = require('express');
const nugu = require('../nugu');
const router = express.Router();

router.post(`/nugu/Set_List`, nugu);
router.post(`/nugu/Delete_List`, nugu);
router.post(`/nugu/Listen_List`, nugu);

module.exports = router;
