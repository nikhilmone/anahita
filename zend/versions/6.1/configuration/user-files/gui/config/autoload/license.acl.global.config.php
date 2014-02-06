<?php
return array(
			'license' => array(
				'acl' => array(
					'ENTERPRISE' => array(),
					'PROFESSIONAL' => array(
						'dataRentention:timelimit' 	=> array('unlimited' => false),
						'auditTrail:timelimit' 	=> array('unlimited' => false),
						'service:Authentication'	=> array('extended' => false),
						'route:UsersWebAPI'			=> array('userAuthenticationSettings' => false),
						'data:components' => array('Zend Java Bridge' => false),
					),
					'SMALL BUSINESS' => array(// Basic
						'route:ServersWebAPI' => array(
							'clusterAddServer' => false,
							'serverAddToCluster' => false
						),
						'service:accessWebAPI'	=> false,
						'dataRentention:timelimit' => array('3month' => false),
						'data:useCustomAction' => false,
						'data:useMonitorAction' => array ('custom' => false),
						'data:components' => array('Zend Session Clustering' => false, 'Zend Job Queue' => false),
						'data:useWebApiKeys' => false,
						'data:showWebApiKeysMarketing' => false,
						'data:editRestartSettings' => false,
						'data:editAuditSettings' => false,
						'data:editNotificationsSettings' => false,
						'route:JobQueueWebApi' => false,
					),
					'DEVELOPER' => array(
							'data:useMultipleUsers' => false,
							'route:JobQueueWebApi' => true,
							'data:components' => array('Zend Job Queue' => true, 'Zend Java Bridge' => true),
					),
					'FREE' => array(
						'data:useMonitorProRuleTypes' => false,
						'data:useMonitorAction' => array ('email' => false),
						'dataRentention:timelimit' => array('2weeks' => false, '1hour' => true),
						'data:useEmailNotification' => false,
						'data:collectEventsCodeTrace' => false,
						'route:UsersWebAPI' => array(false, 'setPassword' => true), /// deny all actions but setPassword, special syntax
						'route:DeploymentWebAPI' => array('applicationRollback' => false),
						'data:components' => array('Zend Job Queue' => false, 'Zend Page Cache' => false, 'Zend Java Bridge' => false),
						'route:PageCacheWebApi' => false,
						'data:showWebApiKeysMarketing' => true,
						'data:hideMarketingContent' => false,
						'data:editSettings' => false,
						'route:JobQueueWebApi' => false,
						'route:ConfigurationWebApi'	=> array('configurationImport' => false, 'configurationExport' => false, 'configurationReset' => false),
					),
					'EMPTY' => array(
						'route:Bootstrap' => true,
						'route:ConfigurationWebAPI' => array('tasksComplete'),
						'route:BootstrapWebAPI' => true,
						'route:Login' => true,
						'route:Expired' => true,
						'route:ServersWebAPI' => array(
							'serverAddToCluster' => true,
							'serverIsInitialized' => true,
							'clusterIsInitialized' => true,
							'restartPhp' => true,
						),
						'route:ConfigurationWebApi' => array(
							'serverStoreLicense' => true,
							'serverValidateLicense' => true,
							'licenseUpdated' => true,
						)
					)
				)
			)
		);