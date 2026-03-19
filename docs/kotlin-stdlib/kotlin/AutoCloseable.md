

# AutoCloseable

Returns an AutoCloseable instance that executes the specified closeAction upon invocation of its close() function.

```kotlin
expect inline fun AutoCloseable(crossinline closeAction: () -> Unit): AutoCloseable(source)
```

```kotlin
fun main() {
    val resource = AutoCloseable {
        println("Resource has been closed")
    }

    resource.use {
        println("Working with resource")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-auto-closeable.html)

    