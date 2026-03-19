

# getStackTraceAddresses

Returns a list of stack trace addresses representing the stack trace pertaining to this throwable.

```kotlin
@ExperimentalNativeApifun Throwable.getStackTraceAddresses(): List<Long>(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi
import kotlin.native.getStackTraceAddresses

@OptIn(ExperimentalNativeApi::class)
fun main() {
    try {
        causeError()
    } catch (e: Exception) {
        val addresses = e.getStackTraceAddresses()
        println("Stack trace addresses:")
        addresses.forEach { addr ->
            println("0x${addr.toString(16)}")
        }
    }
}

fun causeError() {
    throw IllegalStateException("Something went wrong")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-stack-trace-addresses.html)

    