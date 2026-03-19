

# getTimeMillis

Warning since 1.9

```kotlin
external fun getTimeMillis(): Long(source)
```

```kotlin
import kotlin.system.getTimeMillis

fun main() {
    val start = getTimeMillis()

    // Simulate some work
    Thread.sleep(300)

    val end = getTimeMillis()
    println("Elapsed time: ${end - start} ms")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/get-time-millis.html)

    