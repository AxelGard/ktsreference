

# stackTrace

Returns an array of stack trace elements representing the stack trace pertaining to this throwable.

```kotlin
val Throwable.stackTrace: Array<StackTraceElement>(source)
```

```kotlin
fun main() {
    try {
        // code that throws an exception
        throw IllegalArgumentException("Something went wrong")
    } catch (e: Exception) {
        // retrieve the stack trace array
        val trace = e.stackTrace

        // print each stack trace element
        trace.forEach { element ->
            println("${element.className}.${element.methodName}(${element.fileName}:${element.lineNumber})")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/stack-trace.html)

    