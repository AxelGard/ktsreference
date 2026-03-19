

# java

Returns a Java Class instance corresponding to the given KClass instance.

```kotlin
@get:JvmName(name = "getJavaClass")val <T> KClass<T>.java: Class<T>(source)
```

```kotlin
import kotlin.reflect.KClass

fun main() {
    // Obtain the Java Class instance for Kotlin's String type
    val stringJavaClass: Class<String> = String::class.java

    // Use the Java Class as usual
    println("Java class name: ${stringJavaClass.name}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/java.html)

    