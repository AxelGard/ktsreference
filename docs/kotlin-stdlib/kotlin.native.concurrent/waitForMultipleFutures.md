

# waitForMultipleFutures

Wait for availability of futures in the collection. Returns set with all futures which have value available for the consumption, i.e. FutureState.COMPUTED.

```kotlin
@ObsoleteWorkersApifun <T> waitForMultipleFutures(futures: Collection<Future<T>>, timeoutMillis: Int): Set<Future<T>>(source)
```

```kotlin
import kotlin.native.concurrent.*

fun main() {
    val worker = Worker.start()

    // Launch several computations in parallel.
    val futures = (1..5).map { i ->
        worker.execute(TransferMode.SAFE) {
            // Simulate work
            Thread.sleep((i * 200).toLong())
            i * i  // result of the computation
        }
    }

    // Wait up to 1 second for any of the futures to finish.
    val readyFutures = waitForMultipleFutures(futures, timeoutMillis = 1000)

    // Consume the results of the futures that are ready.
    for (future in readyFutures) {
        println("Future ${future.id} completed with value ${future.value}")
    }

    // Shut down the worker.
    worker.requestTermination()
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/wait-for-multiple-futures.html)

    