from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.residue_controller import ResidueController
from app.controllers.company_controller import CompanyController


user_controller = UserController()
residue_controller = ResidueController()
company_controller = CompanyController()

routes = Blueprint('routes', __name__)

# Rotas para User
routes.route('/user', methods=['POST'])(user_controller.create_user)
routes.route('/user/<user_id>', methods=['GET'])(user_controller.get_user)
routes.route('/user', methods=['GET'])(user_controller.get_all_user)
routes.route('/user/<user_id>', methods=['PUT'])(user_controller.update_user)
routes.route('/user/<user_id>', methods=['DELETE'])(user_controller.delete_user)

# Rotas para Residue
routes.route('/residue', methods=['POST'])(residue_controller.create_residue)
routes.route('/residue/<residue_id>', methods=['GET'])(residue_controller.get_residue)
routes.route('/residue', methods=['GET'])(residue_controller.get_all_residue)
routes.route('/residue/<residue_id>', methods=['PUT'])(residue_controller.update_residue)
routes.route('/residue/<residue_id>', methods=['DELETE'])(residue_controller.delete_residue)

# Rotas para Company
routes.route('/company', methods=['POST'])(company_controller.create_company)
routes.route('/company/<company_id>', methods=['GET'])(company_controller.get_company)
routes.route('/company', methods=['GET'])(company_controller.get_all_company)
routes.route('/company/<company_id>', methods=['PUT'])(company_controller.update_company)
routes.route('/company/<company_id>', methods=['DELETE'])(company_controller.delete_company)