from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
import json
import logging

from .generate_gif import generate_trading_gif

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class GenerateGifView(View):
    """
    Django view to generate trading GIFs with SMC analysis.
    """
    
    def post(self, request):
        try:
            # Parse request data
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST.dict()
            
            # Extract parameters with defaults
            symbol = data.get('symbol', 'BTCUSDT')
            start_str = data.get('start_str', '2025-07-28')
            timeframe = data.get('timeframe', '15m')
            window = int(data.get('window', 100))
            limit = int(data.get('limit', 500))
            
            # Validate parameters
            valid_timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d']
            if timeframe not in valid_timeframes:
                return JsonResponse({
                    'error': f'Invalid timeframe. Must be one of: {", ".join(valid_timeframes)}'
                }, status=400)
            
            if window <= 0 or limit <= 0:
                return JsonResponse({
                    'error': 'Window and limit must be positive integers'
                }, status=400)
            
            if limit > 1000:
                return JsonResponse({
                    'error': 'Limit cannot exceed 1000 for performance reasons'
                }, status=400)
            
            # Generate the GIF
            logger.info(f"Generating GIF for {symbol} with params: start={start_str}, timeframe={timeframe}, window={window}, limit={limit}")
            
            gif_buffer = generate_trading_gif(
                symbol=symbol,
                start_str=start_str,
                timeframe=timeframe,
                window=window,
                limit=limit
            )
            
            # Return the GIF as HTTP response
            response = HttpResponse(gif_buffer.getvalue(), content_type='image/gif')
            response['Content-Disposition'] = f'attachment; filename="{symbol}_{timeframe}_analysis.gif"'
            response['Content-Length'] = len(gif_buffer.getvalue())
            
            return response
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            logger.error(f"Error generating GIF: {str(e)}")
            return JsonResponse({
                'error': f'Failed to generate GIF: {str(e)}'
            }, status=500)
    
    def get(self, request):
        """Handle GET requests with query parameters"""
        try:
            # Extract parameters from query string
            symbol = request.GET.get('symbol', 'BTCUSDT')
            start_str = request.GET.get('start_str', '2025-07-28')
            timeframe = request.GET.get('timeframe', '15m')
            window = int(request.GET.get('window', 100))
            limit = int(request.GET.get('limit', 500))
            
            # Validate parameters
            valid_timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d']
            if timeframe not in valid_timeframes:
                return JsonResponse({
                    'error': f'Invalid timeframe. Must be one of: {", ".join(valid_timeframes)}'
                }, status=400)
            
            if window <= 0 or limit <= 0:
                return JsonResponse({
                    'error': 'Window and limit must be positive integers'
                }, status=400)
            
            if limit > 1000:
                return JsonResponse({
                    'error': 'Limit cannot exceed 1000 for performance reasons'
                }, status=400)
            
            # Generate the GIF
            logger.info(f"Generating GIF for {symbol} with params: start={start_str}, timeframe={timeframe}, window={window}, limit={limit}")
            
            gif_buffer = generate_trading_gif(
                symbol=symbol,
                start_str=start_str,
                timeframe=timeframe,
                window=window,
                limit=limit
            )
            
            # Return the GIF as HTTP response
            response = HttpResponse(gif_buffer.getvalue(), content_type='image/gif')
            response['Content-Disposition'] = f'attachment; filename="{symbol}_{timeframe}_analysis.gif"'
            response['Content-Length'] = len(gif_buffer.getvalue())
            
            return response
            
        except ValueError as e:
            return JsonResponse({'error': f'Invalid parameter value: {str(e)}'}, status=400)
        except Exception as e:
            logger.error(f"Error generating GIF: {str(e)}")
            return JsonResponse({
                'error': f'Failed to generate GIF: {str(e)}'
            }, status=500)


def gif_api_info(request):
    """API endpoint to provide information about the GIF generation service"""
    info = {
        'service': 'Trading GIF Generation with SMC Analysis',
        'description': 'Generate animated GIFs of cryptocurrency trading charts with Smart Money Concepts analysis',
        'endpoints': {
            'generate_gif': {
                'url': '/telegram_bot/generate-gif/',
                'methods': ['GET', 'POST'],
                'parameters': {
                    'symbol': {
                        'type': 'string',
                        'default': 'BTCUSDT',
                        'description': 'Trading symbol (e.g., BTCUSDT, ETHUSDT)'
                    },
                    'start_str': {
                        'type': 'string',
                        'default': '2025-07-28',
                        'description': 'Start date for data (YYYY-MM-DD format)'
                    },
                    'timeframe': {
                        'type': 'string',
                        'default': '15m',
                        'options': ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d'],
                        'description': 'Chart timeframe'
                    },
                    'window': {
                        'type': 'integer',
                        'default': 100,
                        'description': 'Rolling window size for analysis'
                    },
                    'limit': {
                        'type': 'integer',
                        'default': 500,
                        'max': 1000,
                        'description': 'Maximum number of candles to process'
                    }
                }
            }
        },
        'examples': {
            'GET': '/telegram_bot/generate-gif/?symbol=BTCUSDT&timeframe=1h&window=50&limit=200',
            'POST': {
                'url': '/telegram_bot/generate-gif/',
                'body': {
                    'symbol': 'ETHUSDT',
                    'start_str': '2025-07-01',
                    'timeframe': '4h',
                    'window': 80,
                    'limit': 300
                }
            }
        }
    }
    return JsonResponse(info, json_dumps_params={'indent': 2})


def home(request):
    """Home page showing available endpoints"""
    context = {
        'title': 'FreyrQA Portal - Telegram Bot API',
        'endpoints': [
            {
                'name': 'API Info',
                'url': '/telegram_bot/api-info/',
                'description': 'Get information about available endpoints'
            },
            {
                'name': 'Generate Trading GIF',
                'url': '/telegram_bot/generate-gif/',
                'description': 'Generate animated trading charts with SMC analysis'
            }
        ]
    }
    return render(request, 'telegram_bot_task/home.html', context)
