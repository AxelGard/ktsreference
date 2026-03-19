

# isInitialized

Returns true if this lateinit property has been assigned a value, and false otherwise.

```kotlin
val KProperty0<*>.isInitialized: Boolean(source)
```

```kotlin
class Example {
    lateinit var message: String

    fun init() {
        message = "Hello, Kotlin!"
    }

    fun printIfInitialized() {
        if (this::message.isInitialized) {
            println(message)
        } else {
            println("message is not initialized")
        }
    }
}

fun main() {
    val example = Example()

    example.printIfInitialized()   // message is not initialized

    example.init()
    example.printIfInitialized()   // Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/is-initialized.html)

    