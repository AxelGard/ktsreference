

# javaClass

Returns the runtime Java class of this object.

```kotlin
val <T : Any> T.javaClass: Class<T>(source)
```

fun <T : Any> printClassName(value: T) {
    println(value.javaClass.name)
}

fun main() {
    val number = 42
    val text = "Hello"
    printClassName(number) // prints java.lang.Integer
    printClassName(text)   // prints java.lang.String
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/java-class.html)

    